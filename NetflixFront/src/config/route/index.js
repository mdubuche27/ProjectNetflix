import React, { useState } from 'react'
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom'

import Modal from '../../component/modal'
import Films from '../../component/medias/films'


import { ThemeProvider } from 'styled-components'
import { useSelector } from 'react-redux'
import { createGlobalStyle } from 'styled-components'

const Routes = () => {
//  const dispatch = useDispatch()
    // const favorites = useSelector(state => state.favorites.pokemons)
//  const setFavorites = fav => dispatch(favoritesActions.set_unset_favorite(fav))


    return(
        <Router>
            <Modal></Modal>
            <Switch>
                <Route path="/films" component={() => <Films />} />
            </Switch>
        </Router>
    )
}

const GlobalStyle = createGlobalStyle`
  body {
    background-color: ${props => props.theme.backgroundColor};
    color : ${props => props.theme.textColor}
  }
`

export default Routes