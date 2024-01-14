import React, { useState, useEffect, createContext} from "react";

export const AuthContext = createContext({
    auth: undefined,
    login: () => null,
    logout: () => null,

});

export function AuthProvider(props) {
    const { children } = props;

    const login = async (token) => {
        console.log('Realizando login--->', token);
    }

    const valueContext = {
        auth: null,
        login,
        logout: () =>console.log('Realizando logout'),
    };


    return (
        <AuthContext.Provider value={valueContext}>{children}</AuthContext.Provider>
    
    );
}