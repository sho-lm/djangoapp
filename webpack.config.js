const path = require('path');

module.exports = {
    // バンドル対象のファイル
    entry:　'./frontend/main.js',
    mode: 'development',
    output: {
        filename: 'bundle.js' ,
        path: path.resolve(__dirname, 'public/assets')
    },
    resolve: {
        
    },
    module: {
        rules:[
            
        ]
    },
    plugins: [

    ],
}