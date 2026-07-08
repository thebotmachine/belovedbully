<script setup>
useBreadcrumbItems({
  overrides: [
    { label: 'Главная' }
  ]
})
</script>

<template>
  <UApp>
    <NuxtLoadingIndicator color="var(--ui-color-neutral-900)"/>
    <NuxtLayout>
      <UMain class="relative">
        <NuxtPage />
      </UMain>
    </NuxtLayout>
  </UApp>
</template>
