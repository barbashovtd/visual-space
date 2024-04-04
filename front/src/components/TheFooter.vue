<template>
  <footer class="footer">
    <div class="container">
      <div class="level">
        <div class="level-left">
          <div id="footer-logo">
            <img class="image is-square is-128x128" src="../assets/logo-big.png" alt="" decoding="async" />
            <h3 class="is-title is-normal" id="footer-logo-text">©Visual Space 2024</h3>
          </div>
        </div>
        <div class="level-item has-text-centered">
          <div class="level subtitle">
            <a class="level-item has-text-centered" href="#description">О нас</a>
            <a class="level-item has-text-centered" href="#advantages">Преимущества</a>
            <a class="level-item has-text-centered" href="#services">Услуги</a>
          </div>
        </div>
        <div class="level-rights">Наши контакты:</div>
      </div>
    </div>
  </footer>
</template>
<script setup></script>
<style scoped>
a {
  color: inherit;
}
.footer {
  border-top: 0.1rem solid #2e2e2e;
}
#footer-logo-text {
  position: relative;
  top: -4rem;
  left: 6rem;
}
</style>
