<script setup lang="ts">
import type {DogListItem} from '~/types/dog'

defineProps<{
  dogs: DogListItem[]
  fromContext?: string
}>()
</script>

<template>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
    <DogsCard v-for="dog in dogs" :key="dog.slug" :dog="dog" :fromContext="fromContext"/>
  </div>
</template>

<style scoped>

</style>