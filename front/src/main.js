import './style.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import axios from 'axios'
// import Tres from '@tresjs/core'

import App from './App.vue'
import router from './router'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)
// app.use(axios);
// app.use(Tres)

app.mount('#app')
