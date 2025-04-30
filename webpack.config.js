const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const { VueLoaderPlugin } = require('vue-loader')
const { CleanWebpackPlugin } = require('clean-webpack-plugin'); // ビルドしたjsファイルの不要になったものを自動で削除する

module.exports = {
    // バンドル対象のファイル
    entry:　'./frontend/main.js',
    mode: 'development',
    output: {
        filename: 'bundle.js' ,
        path: path.resolve(__dirname, 'static/assets')
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
        extensions: ['.vue'],
        modules: [
            'node_modules'
        ],
        alias: {
            'vue': path.resolve('./node_modules/vue/dist/vue.js')
        }
    },
}