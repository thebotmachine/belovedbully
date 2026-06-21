import type {Dog, PaginatedResponse} from '~/types/dog'

export const useDogs = (endpoint: string) => {
    const config = useRuntimeConfig()
    const route = useRoute()
    const router = useRouter()

    const apiBase = config.public.apiBase as string
    const itemsPerPage = 3

    const page = computed({
        get: () => Number(route.query.page) || 1,
        set: (val: number) => router.replace({query: {...route.query, page: val}}),
    })

    const selectedGender = computed({
        get: () => (route.query.gender as string) || null,
        set: (val: string | null) => {
            const query = {...route.query, page: 1}
            if (val) query.gender = val
            else delete query.gender
            router.replace({query})
        },
    })

    const ordering = computed({
        get: () => (route.query.ordering as string) || 'name',
        set: (val: string) => router.replace({query: {...route.query, ordering: val, page: 1}}),
    })

    const query = computed(() => {
        const params: Record<string, string | number> = {page: page.value, ordering: ordering.value}
        if (selectedGender.value) params.gender = selectedGender.value
        return params
    })

    const url = computed(() => endpoint)

    const {data, pending, error} =
        useApi<PaginatedResponse<Dog>>(url, {
            query
        })

    return {
        dogs: computed(() => data.value?.results ?? []),
        pending,
        error,
        page,
        total: computed(() => data.value?.count ?? 0),
        itemsPerPage,
        selectedGender,
        ordering,
    }
}