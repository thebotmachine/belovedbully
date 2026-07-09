<script setup>
useBreadcrumbItems({
  overrides: [
    {label: 'Главная'}
  ]
})

useHead({
  titleTemplate: '%s — Питомник американских булли BelovedBully',
})
</script>

<template>
  <UApp>
    <ScrollToTop/>
    <NuxtLoadingIndicator color="var(--ui-color-neutral-900)"/>

    <AppHeader/>

    <UMain class="bg-elevated">
      <NuxtPage/>
    </UMain>

    <AppFooter/>

  </UApp>
</template>
