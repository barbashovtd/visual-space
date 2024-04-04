<template>
  <TheHeader />
  <div class="section">
    <div class="container">
      <div class="is-unselectable pt-6">
        <h1 class="title is-1 is-spaced has-text-left pt-6 unbounded-title" id="title-main">
          Web Studio<br />helping startup's
        </h1>
        <h3 class="subtitle is-3 pt-2 unbounded-subtitle">Команда, понимающая ваши проблемы</h3>
        <ButtonAppeal size="large" />
      </div>
      <div class="is-relative is-hidden-touch" id="star">
        <Suspense>
          <TheStar />
        </Suspense>
      </div>
      <div id="flares">
        <img src="../assets/flare-small.svg" id="flare-small" />
        <img src="../assets/flare-big.svg" id="flare-big" />
      </div>
    </div>
  </div>
  <div class="section" id="description">
    <div class="container is-relative" id="description-container">
      <div class="fixed-grid has-2-cols" id="description-grid">
        <div class="grid is-relative">
          <div class="cell pl-6 ml-6 unbounded-title">
            <div class="title is-1 has-text-left" id="description-text-tl">
              <h1>Молодая<br />креативная<br />студия</h1>
            </div>
          </div>
          <div class="cell pr-6 mr-6">
            <div class="subtitle is-3 has-text-right" id="description-text-tr">
              <h3>Мы - участники программы<br />ФСИ, понимаем ваши<br />потребности и помогаем с<br />их закрытием</h3>
            </div>
          </div>
          <div class="cell pl-6 ml-6">
            <div class="subtitle is-3 has-text-left pt-4" id="description-text-bl">
              <h3>Разрабатываем сайты<br />понимая ваши проблемы и<br />решая их доступным<br />способом</h3>
            </div>
          </div>
          <div class="cell pr-6 mr-6 unbounded-title">
            <div class="title is-1 has-text-right pt-4" id="description-text-br">
              <h1>Развиваем<br />вас и ваш<br />бренд</h1>
            </div>
          </div>
          <img
            src="../assets/star-center.svg"
            alt=""
            id="flare-center"
            class="is-hidden-touch is-hidden-desktop-only"
          />
          <img
            src="../assets/star-corner.svg"
            alt=""
            id="flare-corner-top"
            class="is-pulled-left is-hidden-touch is-hidden-desktop-only"
          />
          <img
            src="../assets/star-corner.svg"
            alt=""
            id="flare-corner-bottom"
            class="is-hidden-touch is-hidden-desktop-only"
          />
        </div>
      </div>
    </div>
  </div>
  <div class="section" id="advantages">
    <div class="container is-relative" id="advantages-container">
      <h1 class="title is-1 has-text-left unbounded-title pb-6">Преимущества</h1>
      <AdvantageOption
        title="Индивидуальный подход"
        text="Говорим вашим техническим языком. Осознаем тонкости вашего проекта и можем общаться на одном языке с вашей
            командой, что обеспечивает точное понимание ваших нужд и целей"
        point="O1"
      />
      <AdvantageOption
        title="Сэкономленное время"
        text="Сотрудничество с нами позволяет заказчику сосредоточиться на своем бизнесе, не тратя время на создание и поддержку веб-сайта"
        point="O2"
      />
      <AdvantageOption
        title="Качество исполнения"
        text="Предлагаем лучшее соотношение цены и качества. Создаем продукты, доступный для стартапов на разных этапах развития"
        point="O3"
      />
      <AdvantageOption
        title="Технологичность"
        text="Используем современные технологии для создания интерактивных и масштабируемых сайтов, сосредоточенных на адаптацию под ваши потребности"
        point="O4"
      />
    </div>
  </div>
  <div class="section" id="services">
    <div class="container is-relative">
      <h1 class="title is-1 has-text-left unbounded-title">Услуги</h1>
      <ServiceLanding />
      <ServiceBusiness />
    </div>
  </div>

  <TheFooter />
</template>

<script setup>
import TheStar from './TheStar.vue'
import TheHeader from './TheHeader.vue'
import TheFooter from './TheFooter.vue'
import ButtonAppeal from './ButtonAppeal.vue'
import AdvantageOption from './AdvantageOption.vue'
import ServiceLanding from './ServiceLanding.vue'
import ServiceBusiness from './ServiceBusiness.vue'
</script>

<style>
.subtitle {
  color: #cacaca;
}
.title {
  color: #cacaca;
}
#services-container {
  background-color: #121212;
  border-color: #1b1b1b;
  border-width: 1rem;
}
#services-container-inner {
  background-color: #232323;
  border-color: #2e2e2e;
  border-width: 1rem;
}
#flare-small {
  position: relative;
  left: 210px;
  bottom: 160px;
}
#title-main {
  font-size: 7.5rem;
}
#flares {
  position: relative;
  top: -72rem;
  left: -8rem;
  z-index: -2;
  width: 85%;
  height: 85%;
}
#star {
  z-index: -1;
  position: relative;
  top: -35rem;
  left: 35rem;
}
#header-title-button {
  position: relative;
}
#flare-corner-bottom {
  position: absolute;
  rotate: 180deg;
  transform: translateY(10rem);
  -webkit-transform: translateY(10rem);
}
#flare-center {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  -webkit-transform: translateX(-50%);
}
#flare-corner-top {
  transform: translateY(-30rem);
  -webkit-transform: translateY(-30rem);
}
#flare-corner-bottom {
  transform: translate(-105%, -10%);
}
#description-text-tl {
  font-size: 3.5rem;
}
</style>
