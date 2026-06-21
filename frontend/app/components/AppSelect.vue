<script setup lang="ts">
const items = ref(['Backlog', 'Todo', 'In Progress', 'Done'])
const value = ref('Backlog')
const items1: DropdownMenuItem[][] = [
  [
    {
      label: 'View',
      icon: 'i-lucide-eye'
    },
    {
      label: 'Copy',
      icon: 'i-lucide-copy'
    },
    {
      label: 'Edit',
      icon: 'i-lucide-pencil'
    }
  ],
  [
    {
      label: 'Delete',
      color: 'error',
      icon: 'i-lucide-trash'
    }
  ]
]
</script>

<template>

  <UDropdownMenu :items="items1" :ui="{ content: 'w-(--reka-dropdown-menu-trigger-width)' }">
    <UButton
      label="Open"
      class="w-46"
      color="neutral"
      variant="outline"
      block
      trailing-icon="i-lucide-chevron-down"
    />
  </UDropdownMenu>

  <USelect v-model="value" :items="items" />

  <UPopover modal>
    <UButton label="Open" color="neutral" variant="subtle" />

    <template #content>
      <Placeholder class="size-48 m-4 inline-flex" />
    </template>
  </UPopover>

 <UDrawer>
    <UButton
      label="Open"
      class="w-46"
      color="neutral"
      variant="outline"
      block
      trailing-icon="i-lucide-chevron-down"
    />

    <template #content>
      <Placeholder class="h-48 m-4" />
    </template>
  </UDrawer>
</template>