import React, { createContext, useState, useEffect, useContext } from 'react';

// oma authContext
const AuthContext = createContext(null);

// Provider-komponentti on kuin mikä tahansa muukin, react-komponentti (siinä voi käyttää statea ja useEffectiä),
// {children}...children on spesiaali parametrin nimi
// se tarkoittaa , että authprovideria voi käyttää wrappaamaan muita react-komponentteja,
// nämä komponentit, joiden ympärillä authprovideria käytetään on children-parametrissa
export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null); // Optional: store user information
  const [loading, setLoading] = useState(true);

 

  useEffect(() => {
    
    // tehdään reqeust api/auth/account-routeen, josta saa vastauksena sisäänkirjautuneen käyttäjän tiedot (jos käyttäjä on kirjautunut sisään)
    const checkAuthStatus = async () => {
      
      // luetaan token localStoragesta, loginissa se on sinna laitettu  
      const token = localStorage.getItem('authToken');
      try {
        
        setLoading(true)
        const accountRes = await fetch('/api/auth/account', {
            headers: {
                'Content-Type': 'application/json',
                // lähetetään token sekä headerissa, että 
                Authorization: `Bearer ${token}`
            },
            // cookiessa
            credentials: 'include'
        })
        if(!accountRes.ok) {
            throw new Error(accountRes.statusText)
        }
        const data = await accountRes.json()
        setUser(data)
        setIsAuthenticated(true)
        
      } catch(e) {
        setUser(null)
        setIsAuthenticated(false)
      } finally{  
        setLoading(false);
      }
    };

    checkAuthStatus();
  }, []);

  // tätä käytetään Login-komponentissa
  const login = async (credentials) => {
    setLoading(true);
    // Replace this with your actual login API call
    try {
      const response = await fetch('/api/auth/login', { // Assuming you're using the proxy
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
      });

      if (response.ok) {
        const data = await response.json();
        
        localStorage.setItem('authToken', data);
        setIsAuthenticated(true);
        
      } else {
        setIsAuthenticated(false);
        setUser(null);
        // Handle login error (e.g., display a message to the user)
        console.error('Login failed:', await response.text());
        throw new Error('Login failed');
      }
    } catch (error) {
      setIsAuthenticated(false);
      setUser(null);
      console.error('Login error:', error);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  // Function to handle logout
  const logout = () => {
    localStorage.removeItem('authToken');
    setIsAuthenticated(false);
    setUser(null);
    
    
  };

  // The value passed to the context provider
  const authContextValue = {
    isAuthenticated,
    user,
    loading,
    login,
    logout,
  };

  // mikä / mitä tahansa komponentteja chilren sisältääkään, kaikki isAuthenticated, user, loading, logoin ja logout ovat niissä käytettävissä, koska authcontext.provider on sen ympärillä
  return (
    <AuthContext.Provider value={authContextValue}>
      {children}
    </AuthContext.Provider>
  );
};

// isAuthenticated, user, loading, login ja logout ovat saatavilla useAuth-hookin kautta
export const useAuth = () => {
  return useContext(AuthContext);
};