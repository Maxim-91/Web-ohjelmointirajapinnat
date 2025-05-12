import './Login.css'
import { useEffect, useState } from 'react'
import { useAuth } from './AuthContext';
import { useNavigate } from 'react-router-dom';

function Login() {

    


    // tässä on useAuth-hook käytössä
    const { login, isAuthenticated } = useAuth(); 
    const navigate = useNavigate()

    useEffect(() => {
        if(isAuthenticated) {
            navigate('/')
        }
    }, [])

    const _login = async (e) => {
        e.preventDefault()
        login({username, password})
    }

    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const updateUsername = (e) => {
        setUsername(e.target.value)
    }

    const updatePassword = (e) => {
        setPassword(e.target.value)
    }

    // jos käyttäjä on kirjautunut sisään, ohjataan etusivulle takaisin (jos yrittää kirjautuneena login-sivulle)
    

    return (

        <main>
            <form onSubmit={_login} method="POST" action="#">
                <label htmlFor="name">Username:</label>
                

                <input value={username} onChange={updateUsername} type="text" id="name" name="username" required />

                

                <label htmlFor="password">Password:</label>
                
                <input value={password} onChange={updatePassword} type="password" id="password" name="password" required />

                

                <input type="submit" value="Submit" />
            </form>
        </main>
    )

}

export default Login