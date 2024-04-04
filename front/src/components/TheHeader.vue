<template>
  <header>
    <nav class="navbar is-black is-fixed-top" role="navigation" aria-label="main navigation">
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item" href="#">
            <img class="image is-square is-32x32" src="../assets/logo.png" alt="◯" />
          </a>
          <a
            data-target="main-menu"
            class="navbar-burger"
            role="button"
            aria-label="menu"
            :aria-expanded="isExpanded"
            @click="showBurger = !showBurger"
            :class="{ 'is-active': showBurger }"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <div class="navbar-menu pb-3 pt-3">
          <div class="navbar-start" id="main-menu">
            <a href="#description" class="navbar-item">О нас</a>
            <a href="#advantages" class="navbar-item">Преимущества</a>
            <a href="#services" class="navbar-item">Услуги</a>
          </div>
          <div class="navbar-end pt-2" id="navbar-button-appeal"><ButtonAppeal /></div>
        </div>
      </div>
    </nav>
  </header>
</template>
<script setup>
import ButtonAppeal from './ButtonAppeal.vue'
import { ref } from 'vue'
const showBurger = ref(false)
const isExpanded = ref(false)
</script>

<style scoped>
#navbar-button-appeal {
  height: 85%;
}
.navbar {
  border-bottom: 0.1rem solid #2e2e2e;
}
.navbar-item:hover {
  background-color: transparent;
}
#main-menu {
  border-radius: 8rem;
  border-color: #2e2e2e;
  border-style: solid;
  border-width: 0.1rem;
}
</style>
