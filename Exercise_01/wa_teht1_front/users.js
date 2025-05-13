document.addEventListener('DOMContentLoaded', async function() {
    try {
        const res = await fetch('http://localhost:8080/users')
        
        if(!res.ok) {
            throw new Error(res.statusText)
        }
        const responseBody = await res.text()
        document.querySelector("#container").innerHTML = responseBody;
    } catch(e) {
        console.log(e)
    }
})