<script setup lang="ts">
useSeoMeta({
  title: 'Наши выпускники - щенки американского булли из питомника BelovedBully',
  description: 'Щенки, которые уже выросли в питомнике BelovedBully и переехали в новые семьи. Фото повзрослевших питомцев - реальный результат нашей работы с породой.',
  ogTitle: 'Выпускники питомника BelovedBully',
  ogDescription: 'Щенки американского булли, которые уже нашли свой дом.',
})
</script>

<template>
<DogsCatalog endpoint="/graduates/" from-context="graduates" breadcrumb-label="Выпускники" />
</template>

<style scoped>

</style>