import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import VueDevTools from 'vite-plugin-vue-devtools'

import { templateCompilerOptions } from '@tresjs/core'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({ ...templateCompilerOptions }),
    VueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: "http://127.0.0.1:8000/",
    cors: true
  }

  // css: {
  //   preprocessorOptions: {
  //     scss: {
  //       additionalData: `@use "@/style.scss" as *;`
  //     }
  //   }
  // }
})