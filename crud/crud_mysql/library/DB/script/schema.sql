/*===============================================*/
/* DBMS : MySQL 5*								 */
/* Create by : EniDEv911						 */
/*===============================================*/

/*===============================================*/
/*					  SCHEMA					 */
/*===============================================*/




/*===============================================*/
/*					  TABLES					 */
/*===============================================*/


/*===============================================*/
/* Users

CREATE TABLE IF NOT EXISTS `library_db`.`users`(
	`id` BIGINT(11) NOT NULL,
	`first_name` VARCHAR(30) NOT NULL,
	`last_name` VARCHAR(30) NOT NULL,
	`address` VARCHAR(100) NOT NULL,
	`city` VARCHAR(30) NOT NULL,
	`email` VARCHAR(50),
	PRIMARY KEY(`id`)
	)ENGINE=InnoDB;
/*===============================================*/

/*================== AUTHOR ====================*/

CREATE TABLE IF NOT EXISTS `library_db`.`author`(
	`id` BIGINT(20),
	`fullname` VARCHAR(255) NOT NULL,
	`date_of_birth` DATE NOT NULL,
	`date_of_death` DATE NOT NULL,
	PRIMARY key(`id`)
	)ENGINE=InnoDB;

/*================== BOOKS ====================*/

CREATE TABLE IF NOT EXISTS `library_db`.`books`(
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(30) NOT NULL,	
	`gender` VARCHAR(30) NOT NULL,
	`editorial` VARCHAR(40) NOT NULL,
	`release_date` DATE NOT NULL,
	`description` VARCHAR(255),
	`entry_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON 
	UPDATE CURRENT_TIMESTAMP,
	`id_author` BIGINT(20), 
	PRIMARY KEY(`id`),
	CONSTRAINT `author` FOREIGN KEY(`id_author`) REFERENCES `library_db`.`author`(`id`)
	)ENGINE=InnoDB;
