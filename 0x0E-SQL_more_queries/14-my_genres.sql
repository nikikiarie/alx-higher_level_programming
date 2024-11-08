-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT z.`name`
  FROM `tv_genres` AS z
       INNER JOIN `tv_show_genres` AS a
       ON z.`id` = a.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON t.`id` = a.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY z.`name`;
 