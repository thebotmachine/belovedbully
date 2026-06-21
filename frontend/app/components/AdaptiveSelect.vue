<script setup lang="ts" generic="T">
interface Option {
  label: string
  value: T
}

interface Props {
  label: string
  options: Option[]
  modelValue: T
  direction?: 'top' | 'bottom' | 'left' | 'right'
  ui?: any
}

const props = withDefaults(defineProps<Props>(), {
  direction: 'bottom',
})

const emit = defineEmits<{
  'update:modelValue': [value: T]
}>()

const dropdownOpen = ref(false)
const drawerOpen = ref(false)

const dropdownItems = computed(() =>
    props.options.map(opt => ({
      label: opt.label,
      icon: opt.value === props.modelValue ? 'i-lucide-check' : undefined,
      active: opt.value === props.modelValue,
      ui: {item: 'focus:outline-none'},
      onSelect() {
        handleSelect(opt.value)
      },
    }))
)

function handleSelect(value: T) {
  emit('update:modelValue', value)
  dropdownOpen.value = false
  drawerOpen.value = false
}
</script>

<template>
  <div>
    <div class="hidden md:block">
      <UDropdownMenu
          v-model:open="dropdownOpen"
          :items="dropdownItems"
          :ui="{ content: 'w-(--reka-dropdown-menu-trigger-width)' }"
      >
        <UButton
            color="neutral"
            variant="outline"
            block
            class="justify-between"
            :ui="ui"
        >
          <span class="flex items-center gap-1">
            <span class="text-muted">{{ label }}:</span>
            <span class="text-medium">
              {{ options.find(o => o.value === modelValue)?.label || '...' }}
            </span>
          </span>

          <template #trailing>
            <UIcon
                name="i-lucide-chevron-down"
                class="size-5 transition-transform duration-200"
                :class="{ 'rotate-180': dropdownOpen }"
                aria-hidden="true"
            />
          </template>
        </UButton>
      </UDropdownMenu>
    </div>

    <div class="block md:hidden">
      <UDrawer
          v-model:open="drawerOpen"
      >
        <UButton
            color="neutral"
            variant="outline"
            block
            class="justify-between"
            :ui="ui"
            @click="drawerOpen = true"
        >
          <span class="flex items-center gap-1">
            <span class="text-muted">{{ label }}:</span>
            <span class="text-medium">
              {{ options.find(o => o.value === modelValue)?.label || '...' }}
            </span>
          </span>

          <template #trailing>
            <UIcon
                name="i-lucide-chevron-down"
                class="size-5 transition-transform duration-200"
                :class="{ 'rotate-180': drawerOpen }"
                aria-hidden="true"
            />
          </template>
        </UButton>

        <template #body>
          <div class="flex items-center justify-between gap-4 mb-4">
            <h2 class="text-highlighted font-semibold">{{ label }}</h2>

            <UButton color="neutral" variant="soft" icon="i-lucide-x" @click="drawerOpen = false"/>
          </div>

          <div class="flex flex-col gap-1 p-4">
            <UButton
                v-for="opt in options"
                :key="opt.label"
                :label="opt.label"
                variant="ghost"
                color="neutral"
                size="lg"
                block
                :icon="opt.value === modelValue ? 'i-lucide-check' : undefined"
                :ui="{ base: opt.value === modelValue ? 'bg-elevated' : '' }"
                @click="handleSelect(opt.value)"
            />
          </div>
        </template>
      </UDrawer>
    </div>
  </div>
</template>