import type {Dog} from '~/types/dog'


export const useDogs_v2 = () => {
    const {data, pending, error} = useApi<Dog[]>('/puppies/')
    return {
        dogs: data,
        pending,
        error,
    }
}