-- Lists all genres from the database hbtn_0d_tvshows along with
-- the number of shows linked to each in asc order by genre name.

SELECT z.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS z
       INNER JOIN `tv_show_genres` AS a
       ON z.`id` = a.`genre_id`
 GROUP BY z.`name`
 ORDER BY `number_of_shows` DESC;
 