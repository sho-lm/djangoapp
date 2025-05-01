import { createApp } from 'vue' // Vue3の書き方

import App from './App'

// Vue3オブジェクト
const app = createApp(App)
app.mount('#app')

// babel変換の確認用
const test = () => console.log('hello');
test();