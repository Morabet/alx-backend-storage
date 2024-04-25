-- creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser; 
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE sum_of_fac INT;
    DECLARE weighted_score DECIMAL(10, 2);

    -- Calculate the sum of weights for projects related to the user
    SELECT SUM(weight) INTO sum_of_fac 
    FROM projects 
    WHERE id IN (SELECT project_id FROM corrections WHERE user_id = user_id);

    -- Calculate the weighted score for the user
    SELECT SUM(weight * score) / sum_of_fac INTO weighted_score 
    FROM projects
    JOIN corrections ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;

    UPDATE users SET average_score = weighted_score WHERE id = user_id;
    
    -- Return the computed weighted score
    SELECT weighted_score AS Message;
END //

DELIMITER ;
