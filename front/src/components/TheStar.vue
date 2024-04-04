<template>
  <div class="tres-container">
    <TresCanvas v-bind="gl">
      <TresPerspectiveCamera :position="[0, 0.18, 0.18]" />
      <OrbitControls :auto-rotate="true" />
      <Suspense>
        <TheModel />
      </Suspense>
      <TresDirectionalLight :position="[-2, 6, -8]" :intensity="1" color="#e6e6e6" />
      <TresAmbientLight :intensity="1" />
    </TresCanvas>
  </div>
</template>
<script setup>
import { TresCanvas } from '@tresjs/core'
import { OrbitControls } from '@tresjs/cientos'
import { BasicShadowMap, SRGBColorSpace, NoToneMapping } from 'three'
import TheModel from './TheModel.vue'

const gl = {
  clearColor: '#0f0f0f',
  shadows: false,
  alpha: true,
  shadowMapType: BasicShadowMap,
  outputColorSpace: SRGBColorSpace,
  toneMapping: NoToneMapping
}
</script>
<style>
.tres-container {
  width: 640px;
  height: 640px;
}

/* canvas {
  width: 100%;
  height: 100%;
} */
</style>
