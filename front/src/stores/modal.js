import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useModalStore = defineStore('modal', () => {
  const modalWindowShow = ref(false)
  function show() {
    modalWindowShow.value = true
  }
  function close() {
    modalWindowShow.value = false
  }

  return { modalWindowShow, show, close }
})
