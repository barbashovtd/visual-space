<template>
  <primitive :object="model" />
</template>

<script setup>
import { useGLTF } from '@tresjs/cientos'

const { nodes } = await useGLTF('well_done.glb', { draco: true })
const model = nodes.Curve
</script>
