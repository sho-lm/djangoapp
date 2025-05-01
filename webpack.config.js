const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const { VueLoaderPlugin } = require('vue-loader')
const { CleanWebpackPlugin } = require('clean-webpack-plugin'); // ビルドしたjsファイルの不要になったものを自動で削除する

module.exports = {
    // バンドル対象のファイル
    entry:　'./frontend/index.js',
    mode: 'development',
    output: {
        filename: 'bundle.js' ,
        path: path.resolve(__dirname, 'static/build')
    },
    plugins: [
        new BundleTracker({
            path: '.',
            filename: 'webpack-stats.json'
        }),
        new CleanWebpackPlugin({
            verbose: true
        }),
        new VueLoaderPlugin()
    ],
    module: {
        rules:[
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            }
        ]
    },
    resolve: {
        // import 文で拡張子を省略できる
        extensions: ['.js', '.ts', '.vue', '.css', '.scss'],
        alias: {
        }
    },
}