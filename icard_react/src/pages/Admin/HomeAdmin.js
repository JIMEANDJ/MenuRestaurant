import React from 'react'; 
import {useAuth} from "../../hooks";

export function HomeAdmin() {
const { logout } = useAuth();
  return (
    <div className='welcome-admin'>
        <h1 className='welcome-admin-h1'>Hola</h1> 
        <button onClick={logout}>Cerrar Sesion</button>   

    </div>
  )
}
