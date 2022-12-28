import { Link } from 'react-router-dom'
import { useContext } from 'react';

import classes from'./MainNavigation.module.css'
import FavouritesContext from '../../store/favourites-context';

function MainNavigation() {
  const favouritesCtx = useContext(FavouritesContext);

  return (
    <header className={classes.header}>
      <div>React Meeetups</div>
      <nav>
        <ul>
          <li>
            <Link to=''>All Meetups</Link>
          </li>
          <li>
            <Link to='/new-meetup'>New Meetup</Link>
          </li>
          <li>
            <Link to='/favourites'>
              My Favourite
              <span className={classes.badge}>{favouritesCtx.totalFavourites}</span></Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}
export default MainNavigation;