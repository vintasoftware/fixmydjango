var ProvidePlugin = require('webpack/lib/ProvidePlugin');
var BundleTracker = require('webpack-bundle-tracker');
var webpack = require('webpack')
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var path = require('path');
var node_modules_dir = path.resolve(__dirname, 'node_modules');
var autoprefixer = require('autoprefixer');
var SpritesmithPlugin = require('webpack-spritesmith');

module.exports = {
  context: __dirname,
  entry: [
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/only-dev-server',
    // 'bootstrap-loader/extractStyles',
    'bootstrap-sass!./bootstrap-sass.config.js',
    './assets/js/index',
  ],
  output: {
    path: path.resolve('./assets/bundles/'),
    publicPath: 'http://localhost:3000/assets/bundles/',
    filename: 'bundle.js',
  },
  module: {
    loaders: [
      {
        test: /\.css$/,
        loaders: [
          'style',
          'css',
          'postcss',
        ],
      },
      {
        test: /\.scss$/,
        loaders: [
          'style',
          'css',
          'postcss',
          'sass',
        ],
      },
      {
        test:/bootstrap-sass[\/\\]assets[\/\\]javascripts[\/\\]/,
        loader: 'imports?jQuery=jquery' },
      {
        test: /\.jsx?$/,
        exclude: [node_modules_dir],
        loaders: ['react-hot', 'babel?presets[]=react,presets[]=es2015']
      },
      {
        test: /\.(woff(2)?|eot|ttf|svg)(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=100000'
      },
      {
        test: /\.(jpg|png)?$/,
        loaders: [
          'file?name=i-[hash].[ext]'
        ]
      }
    ]
  },
  postcss: [autoprefixer],
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(), // don't reload if there is an error
    new SpritesmithPlugin({
        src: {
          cwd: path.resolve(__dirname, 'assets/images/'),
          glob: '*.png'
        },
        target: {
          image: path.resolve(__dirname, 'assets/images/spritesmith-generated/sprite.png'),
          css: path.resolve(__dirname, 'assets/sass/vendor/spritesmith.scss')
        },
        retina: '@2x'
    }),
    // new ExtractTextPlugin('bundle.css',{allChunks: true}),
    new BundleTracker({
      filename: './webpack-stats.json'
    })
  ],
  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  }
};