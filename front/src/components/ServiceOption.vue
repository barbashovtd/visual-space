<template>
  <div class="box">
    <h5 class="title is-5 pb-3 unbounded-title">{{ props.title }}</h5>
    <h5 class="subtitle is-5">{{ props.text }}</h5>
  </div>
</template>
<script setup>
const props = defineProps({
  title: { type: String, required: true },
  text: { type: String, required: true }
})
</script>
<style scoped>
.box {
  border-color: #7a7a7a;
  background-color: #4d4d4d;
  box-shadow: none;
}
</style>
