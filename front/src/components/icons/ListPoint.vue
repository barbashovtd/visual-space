<template>
  <div>
    <h3 class="title is-3 unbounded-title">{{ props.text }}</h3>
  </div>
  <div class="is-hidden-touch" id="icon-flares">
    <img src="../../assets/icon-flares.svg" alt="" />
  </div>
</template>
<script setup>
const props = defineProps({ text: { type: String, required: true } })
</script>
<style scoped>
#icon-flares {
  transform: translate(-30%, -45%);
  z-index: -10;
  position: absolute;
}
</style>
