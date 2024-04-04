<template>
  <button :class="`button is-${props.size} is-responsive is-rounded`" @click="modalStore.show()">
    Оставить заявку
  </button>
  <ModalAppeal :active="modalStore.modalWindowShow" />
</template>
<script setup>
import ModalAppeal from './ModalAppeal.vue'
import { useModalStore } from '@/stores/modal'
const modalStore = useModalStore()
const props = defineProps({ size: { type: String, default: 'normal' } })
</script>
<style scoped lang="scss">
button:hover {
  background-color: linear-gradient(90deg, rgba(142, 45, 226, 1) -10%, rgba(74, 0, 224, 1) 110%);
}
button {
  transition-property: background-color;
  transition-duration: 1;
  transition-timing-function: cubic-bezier(0.5, 1, 0.89, 1);
}
</style>
