<script setup lang="ts">
useSeoMeta({
  title: 'Производители американского булли - кобели и суки питомника',
  description: 'Производители питомника BelovedBully - титулованные кобели и суки американского булли с проверенной родословной. Здоровье, экстерьер и характер, которые передаются щенкам.',
  ogTitle: 'Производители американского булли - питомник BelovedBully',
  ogDescription: 'Титулованные производители с проверенной родословной - основа будущих пометов.',
})
</script>

<template>
  <DogsCatalog endpoint="/producers/" from-context="producers" breadcrumb-label="Производители" />
</template>