-- Creates a stored procedure ComputeAverageScoreForUser that
-- computes and stores the average score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN

DECLARE user_score DECIMAL(10, 2);

SELECT AVG(score) INTO user_score FROM corrections WHERE user_id = user_id;

UPDATE users SET average_score = user_score WHERE id = user_id;

END//

DELIMITER ;