import numpy as np

from ggnes.datasets.sensor_fusion import (
    SensorFusionConfig,
    generate_sensor_fusion_dataset,
)


def test_sensor_fusion_deterministic_generation():
    cfg = SensorFusionConfig(samples=256, seed=1234, noise_sigma=0.05)
    X1, y1 = generate_sensor_fusion_dataset(cfg)
    X2, y2 = generate_sensor_fusion_dataset(cfg)

    assert X1.shape == (256, 18)
    assert y1.shape == (256,)
    np.testing.assert_allclose(X1, X2, atol=1e-7)
    np.testing.assert_allclose(y1, y2, atol=1e-7)


def test_sensor_fusion_noise_parameter_influences_targets():
    base_cfg = SensorFusionConfig(samples=2048, noise_sigma=0.0, seed=42)
    noisy_cfg = SensorFusionConfig(samples=2048, noise_sigma=0.3, seed=42)

    _, y_clean = generate_sensor_fusion_dataset(base_cfg)
    _, y_noisy = generate_sensor_fusion_dataset(noisy_cfg)

    assert np.std(y_clean) > 0.0
    assert np.std(y_noisy) > np.std(y_clean)

