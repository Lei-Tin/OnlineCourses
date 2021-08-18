  function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %


    pv = sum(theta' .* X, 2); % pv are the predicted values
    dpvy = pv - y; % Difference between pv and y
    
    n = length(theta);
    
    for i = 1:n
      
      delta(i) = (1/m)*sum(dpvy .* X(:, i));
      
      temp(i) = theta(i) - (alpha * delta(i));
    end;
    
    computeCostMulti(X, y, theta)
    theta
    pause(3)
    
    theta = temp(:);
    

    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCostMulti(X, y, theta);

end

end
