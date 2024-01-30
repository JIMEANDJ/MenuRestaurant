import React from 'react'
import {Menu, Icon } from "semantic-ui-react";
import {Link, useLocation} from "react-router-dom";
import "./SideMenu.scss";

export  function SideMenu(props) {
    
    const {children} = props;
    const {pathname} = useLocation();


    return (
        <>
        
     {/* <div className='side_menu_admin'>
          <MenuLeft pathname={pathname}/>
          <div className='content'>{children}</div>
     </div> */}
        </>
  )
}


function MenuLeft(props) {
    const {pathname} = props;
    
    return (
        <Menu fixed='left' borderless className='side' vertical>
            <Menu.Item as={Link}to ={'/admin'} active = {pathname === "/admin"}>
                <Icon name='home' /> Pedidos 
            </Menu.Item>

            <Menu.Item as={Link}to ={'/admin/tables'} active = {pathname === "/admin/tables"}>
                <Icon name='table' /> Mesas
            </Menu.Item>

            <Menu.Item as={Link}to ={'/admin/payments-history'} active = {pathname === "/admin/payments-history"}>
                <Icon name='table' /> Historial de Pago
            </Menu.Item>

            <Menu.Item as={Link}to ={'/admin/categorias'} active = {pathname === "/admin/categorias"}>
                <Icon name='folder' /> Categorias
            </Menu.Item>

            <Menu.Item as={Link}to ={'/admin/productos'} active = {pathname === "/admin/productos"}>
                <Icon name='cart' /> Productos
            </Menu.Item>
            
            <Menu.Item as={Link}to ={'/admin/users'} active = {pathname === "/admin/users"}>
                <Icon name='users' /> Usuarios
            </Menu.Item>


        </Menu>
    )

}