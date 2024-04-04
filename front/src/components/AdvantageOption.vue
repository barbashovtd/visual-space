<template>
  <div class="advantage-container columns">
    <div class="advantage-text-container column is-three-quarters">
      <h3 class="title is-2 unbounded-title is-spaced">{{ props.title }}</h3>
      <h5 class="subtitle is-4">
        <!-- Говорим вашим техническим языком. Осознаем тонкости вашего проекта и можем общаться на одном языке с вашей
        командой, что обеспечивает точное понимание ваших нужд и целей -->
        {{ props.text }}
      </h5>
    </div>
    <div class="column is-unselectable is-relative">
      <ListPoint :text="props.point" class="list-point" />
    </div>
  </div>
  <hr class="mb-6" />
</template>
<script setup>
import ListPoint from './icons/ListPoint.vue'
const props = defineProps({
  title: { type: String, required: true },
  text: { type: String, required: true },
  point: { type: String, required: true }
})
</script>
<style scoped>
.list-point {
  left: 50%;
  transform: translateX(50%);
}
hr {
  width: 80%;
  color: #e6e6e6;
  opacity: 70%;
}
</style>
