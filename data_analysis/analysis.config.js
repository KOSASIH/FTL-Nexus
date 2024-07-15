export default {
  data_preprocessing: {
    algorithm: 'pca',
    components: 5
  },
  feature_engineering: {
    method: 'ecursive_feature_elimination',
    num_features: 10
  },
  model_training: {
    algorithm: 'random_forest',
    num_estimators: 100
  },
  model_evaluation: {
    metric: 'accuracy',
    threshold: 0.9
  },
  data_visualization: {
    library: 'atplotlib',
    theme: 'dark'
  }
};
