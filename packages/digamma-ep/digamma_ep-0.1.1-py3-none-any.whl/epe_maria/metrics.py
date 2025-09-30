import numpy as np

def phi(reference, current):
    """
    Métrica base de divergência entre dois vetores.
    Pode ser a norma da diferença ou algo mais sofisticado.
    """
    return np.linalg.norm(reference - current)

def delta_phi(reference, current):
    """
    Diferença entre phi(reference, current) e phi(reference, reference).
    Mede o quanto o modelo atual se afasta do baseline.
    """
    baseline_score = phi(reference, reference)
    current_score = phi(reference, current)
    return current_score - baseline_score
