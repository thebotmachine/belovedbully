<script setup lang="ts">
import type {Litter} from '~/types/litter'

defineProps<{
  litters: Litter[]
}>()
</script>

<template>
  <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
    <LittersCard v-for="litter in litters" :key="litter.id" :litter="litter"/>
  </div>
</template>

<style scoped>

</style>