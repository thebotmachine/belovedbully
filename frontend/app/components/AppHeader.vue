<script setup lang="ts">
import type {NavigationMenuItem} from '@nuxt/ui'

const route = useRoute()
const activeSection = computed(() => {
  if (route.path.startsWith('/dogs/')) {
    return route.query.from as string | undefined
  }
  return undefined
})


const items = computed<NavigationMenuItem[]>(() => [
  {
    label: 'Главная',
    to: '/',
    exact: true
  },
  {
    label: 'О питомнике',
    to: '/about',
  },
  {
    label: 'Свободные щенки',
    to: '/puppies',
    active: route.path.startsWith('/puppies') || activeSection.value === 'puppies'
  },
  {
    label: 'Производители',
    to: '/producers',
    active: route.path.startsWith('/producers') || activeSection.value === 'producers'
  },
  {
    label: 'Пометы',
    to: '/litters',
    active: route.path.startsWith('/litters') || activeSection.value === 'litters'
  },
  {
    label: 'Наши выпускники',
    to: '/graduates',
    active: route.path.startsWith('/graduates') || activeSection.value === 'graduates'
  }
])
</script>

<template>
  <UHeader mode="drawer"
           :ui="{
    root: 'border-b-2 border-accented'
  }">
    <template #title>
      <div class="flex items-center gap-2">
        <Logo class="w-8 h-8"/>
        <h1 class="text-2xl font-serif">BelovedBully</h1>
      </div>
    </template>

    <UNavigationMenu :items="items"/>

    <template #right>

      <UButton
          class="hidden md:flex"
          color="neutral"
          variant="outline"
          size="lg"
          icon="i-lucide-phone"
          label="+7 968 821 26 21"
          to="tel:+79688212621"
      />
    </template>

    <template #body>
      <div class="space-y-2">
        <UNavigationMenu :items="items" orientation="vertical" class="-mx-2.5"/>
        <UButton
            color="neutral"
            variant="outline"
            size="lg"
            icon="i-lucide-phone"
            label="+7 968 821 26 21"
            to="tel:+79688212621"
        />
      </div>
    </template>
  </UHeader>
</template>
