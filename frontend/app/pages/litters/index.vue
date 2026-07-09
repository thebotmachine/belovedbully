<script setup lang="ts">


const {data: litters, pending, error} = useLitters()

const items = useBreadcrumbItems()
definePageMeta({
  breadcrumbLabel: 'Помёты'
})

const sortOptions = [
  { label: 'А → Я', value: 'name' },
  { label: 'Я → А', value: '-name' },
]

useSeoMeta({
  title: 'Помёты американского булли',
  description: 'Все помёты питомника BelovedBully: даты рождения, родители, количество кобелей и сук в каждом помёте. Следите за пополнением или выбирайте щенка из конкретной вязки.',
  ogTitle: 'Помёты питомника BelovedBully',
  ogDescription: 'Помёты американского булли от титулованных родителей - даты рождения, состав, родители.',
})
</script>

<template>
    <UContainer class="py-8 space-y-4">
      <UBreadcrumb :items="items" class="mb-8"/>
      <div class="flex flex-row gap-2">
        <AdaptiveSelect v-model="ordering" label="Сортировка" :options="sortOptions" class="w-48" />
      </div>
      <LittersGrid v-if="litters?.length" :litters="litters"/>
      <div v-else-if="pending">Загрузка...</div>
      <div v-else-if="error">Не удалось загрузить список.</div>
      <div v-else>Список пуст.</div>
    </UContainer>
</template>

<style scoped>

</style>