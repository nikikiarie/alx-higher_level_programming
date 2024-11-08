-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Results must be sorted in descending order by their rating
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS z
       INNER JOIN `tv_show_genres` AS a
       ON a.`genre_id` = z.`id`

       INNER JOIN `tv_show_ratings` AS j
       ON j.`show_id` = a.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
