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
</script>

<template>
  <div class="h-screen bg-elevated">
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
  </div>
  <testcard/>
</template>

<style scoped>

</style>