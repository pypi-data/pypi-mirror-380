from epe_maria.metrics import phi, delta_phi
from epe_maria.temporal import second_order_divergence

class EpeMonitor:
    def __init__(self, baseline_model):
        self.baseline = baseline_model
        self.history = []

    def check_anomaly(self, current_model):
        phi_score = phi(self.baseline, current_model)
        delta_score = delta_phi(self.baseline, current_model)
        delta2_score = second_order_divergence(self.baseline, current_model)

        self.history.append({
            "ϝ": phi_score,
            "δϝ": delta_score,
            "δ²ϝ": delta2_score
        })

        if delta2_score > 5:
            return "CRITICAL"
        elif delta_score > 2:
            return "WARNING"
        else:
            return "SAFE"

    def get_history(self):
        return self.history
