export default defineEventHandler(async (event) => {
    const config = useRuntimeConfig(event)
    const body = await readBody(event)
    const data = fetch(`${config.api_v1}/accounts/login/`, {
        body: JSON.stringify(body)
    })
    return data
})