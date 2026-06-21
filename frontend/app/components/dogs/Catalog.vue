<script setup lang="ts">
const props = defineProps<{
  endpoint: string
  fromContext: string
  breadcrumbLabel: string
}>()

const { dogs, pending, error, page, total, itemsPerPage, selectedGender, ordering } = useDogs(props.endpoint)

definePageMeta({
  breadcrumbLabel: props.breadcrumbLabel
})

const breadcrumbItems = useBreadcrumbItems({
  overrides: [undefined, { label: props.breadcrumbLabel }]
})

const genderOptions = [
  { label: 'Все', value: null },
  { label: 'Мальчики', value: 'male' },
  { label: 'Девочки', value: 'female' },
]

const sortOptions = [
  { label: 'А → Я', value: 'name' },
  { label: 'Я → А', value: '-name' },
]
</script>

<template>
  <div class="bg-elevated min-h-screen">
    <UContainer class="py-8 space-y-4">
      <UBreadcrumb :items="breadcrumbItems" class="mb-8" />

      <div class="flex flex-row gap-2">
        <AdaptiveSelect v-model="selectedGender" label="Пол" :options="genderOptions" class="w-48" />
        <AdaptiveSelect v-model="ordering" label="Сортировка" :options="sortOptions" class="w-48" />
      </div>

      <DogsGrid :dogs="dogs" :fromContext="props.fromContext" />

      <div class="flex justify-center mt-8">
        <UPagination
          v-if="total > 0"
          v-model:page="page"
          :total="total"
          :items-per-page="itemsPerPage"
          show-controls
          show-edges
          size="md"
          active-color="neutral"
        />
      </div>
    </UContainer>
  </div>
</template>