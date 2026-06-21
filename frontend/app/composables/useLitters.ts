import type {Litter} from '~/types/litter'


export const useLitters = () => {

    return useApi<Litter[]>('/litters/', {
        key: 'litters',
        default: () => [],
    })

}