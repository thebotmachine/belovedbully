export const useApi = createUseFetch((callerOptions) => {
  const config = useRuntimeConfig()

  const baseURL = import.meta.server
    ? (config.apiUrl as string)
    : (config.public.apiUrl as string)

  return {
    baseURL,
    ...callerOptions,
  }
})