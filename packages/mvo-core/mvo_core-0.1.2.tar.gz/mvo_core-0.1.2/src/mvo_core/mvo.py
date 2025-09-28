# mvo_core.py
import numpy as np
from scipy.stats import pearsonr, t
from sklearn.utils import resample
from sklearn.metrics import roc_curve, auc, brier_score_loss
from sklearn.linear_model import LogisticRegression
from lifelines.utils import concordance_index


class MVOResult:
    """自定义返回类，只显示指标，不默认打印预测概率"""

    def __init__(self, auc, brier, cindex=None, y_pred_prob=None, vec_final=None):
        self.auc = auc
        self.brier = brier
        self.cindex = cindex
        self.y_pred_prob = y_pred_prob
        self.vec_final = vec_final  # 保存最终优化向量

    def __repr__(self):
        rep = f"AUC: {self.auc}\nBrier: {self.brier}"
        if self.cindex is not None:
            rep += f"\nC-index: {self.cindex}"
        return rep


class MVO:
    """MVO algorithm for mortality vector optimization"""

    def normalize_columns_vec(self, X, y):
        """Normalize columns to [-1,1] and generate initial mortality vector"""
        X = np.array(X, dtype=float)
        y = np.array(y, dtype=float)
        min_vals = np.nanmin(X, axis=0)
        max_vals = np.nanmax(X, axis=0)
        range_vals = max_vals - min_vals
        range_vals[range_vals == 0] = 1
        X_norm = 2 * (X - min_vals) / range_vals - 1

        vec = []
        for i in range(X.shape[1]):
            col = X[:, i]
            if np.all(col == col[0]):
                vec.append(0)
            else:
                corr, _ = pearsonr(col, y)
                vec.append(1 if corr >= 0 else -1)
        return X_norm, np.array(vec, dtype=float)

    def pro_list(self, vec, mat):
        vec = np.array(vec, dtype=float)
        projections = []
        for i in range(mat.shape[0]):
            row = np.array(mat[i], dtype=float)
            projections.append(np.dot(row, vec) / np.linalg.norm(vec))
        return projections

    def AUC_pro(self, y, mat, vec):
        pro = self.pro_list(vec, mat)
        fpr, tpr, _ = roc_curve(y, pro)
        return auc(fpr, tpr), np.array(pro)

    def pa_de_pro(self, vec, y, mat, delta):
        deriv = []
        for i in range(len(vec)):
            vec_new = vec.copy()
            vec_new[i] += delta if vec_new[i] >= 0 else -delta
            deriv.append((self.AUC_pro(y, mat, vec_new)[0] - self.AUC_pro(y, mat, vec)[0]) / delta)
        return deriv

    # 占位优化函数，可自行替换成真正的 MVO 优化逻辑
    def optimize_vec_figure_break_pro(self, vec, y, X, delta, n_iter):
        best_vec = vec.copy()
        best_auc, _ = self.AUC_pro(y, X, best_vec)
        for _ in range(n_iter):
            cand_vec = best_vec.copy()
            i = np.random.randint(len(vec))
            cand_vec[i] += np.random.choice([-delta, delta])
            cand_auc, _ = self.AUC_pro(y, X, cand_vec)
            if cand_auc > best_auc:
                best_vec = cand_vec
                best_auc = cand_auc
        return best_vec, best_auc

    def run_mvo_full(self, X, y, n_bootstrap=1, delta=0.1, n_iter=50, los=None):
        X_norm, vec = self.normalize_columns_vec(X, y)
        # Multi-stage optimization
        vec_stage1, _ = self.optimize_vec_figure_break_pro(vec, y, X_norm, delta, n_iter)
        vec_stage2, _ = self.optimize_vec_figure_break_pro(vec_stage1, y, X_norm, delta / 10, n_iter)
        vec_final, _ = self.optimize_vec_figure_break_pro(vec_stage2, y, X_norm, delta / 100, n_iter)

        # Bootstrap evaluation
        auc_list, brier_list, cindex_list = [], [], []
        y_pred_prob_final = None

        for b in range(n_bootstrap):
            idx = resample(np.arange(len(y)))
            X_bs = X_norm[idx]
            y_bs = np.array(y)[idx]
            auc_val, pro = self.AUC_pro(y_bs, X_bs, vec_final)
            auc_list.append(auc_val)

            pro = np.array(pro).reshape(-1, 1)
            model = LogisticRegression()
            model.fit(pro, y_bs)
            y_pred_prob = model.predict_proba(pro)[:, 1]
            brier_list.append(brier_score_loss(y_bs, y_pred_prob))

            if b == n_bootstrap - 1:
                y_pred_prob_final = y_pred_prob

            if los is not None:
                los_bs = np.array(los)[idx]
                cindex_list.append(concordance_index(los_bs, -y_pred_prob, y_bs))

        def mean_ci(lst):
            mean_val = np.mean(lst)
            if n_bootstrap > 1:
                ci = t.interval(0.95, len(lst) - 1, loc=mean_val, scale=np.std(lst, ddof=1) / np.sqrt(len(lst)))
                return {"mean": mean_val, "ci": ci}
            else:
                return {"mean": mean_val}

        return MVOResult(
            auc=mean_ci(auc_list),
            brier=mean_ci(brier_list),
            cindex=mean_ci(cindex_list) if los is not None else None,
            y_pred_prob=y_pred_prob_final,
            vec_final=vec_final  # 保存最终向量
        )
