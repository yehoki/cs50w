import classes from './Card.module.css';

function Card(props) {
    return <div className={classes.card}>
        {props.children}
    </div>
}
export default Card;

//props.children displays all content inbetween opening
// and closing <Card>