package com.hoangvinh.bai2.services;

import com.hoangvinh.bai2.dto.UserCreateRequest;
import com.hoangvinh.bai2.dto.UserResponse;
import com.hoangvinh.bai2.mappers.UserMapper;
import com.hoangvinh.bai2.model.User;
import com.hoangvinh.bai2.repositories.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.NoSuchElementException;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final UserMapper userMapper;

    public List<UserResponse> getAllUsers() {
        return userRepository.findAll().stream()
                .map(userMapper::toResponse)
                .toList();
    }

    public UserResponse findUserById(Long id) {
        User user = userRepository.findById(id).orElseThrow(NoSuchElementException::new);
        return userMapper.toResponse(user);
    }

    public UserResponse createUser(UserCreateRequest userCreateRequest) {
        User user = User.builder()
                .email(userCreateRequest.getEmail())
                .username(userCreateRequest.getUsername())
                .build();
        return userMapper.toResponse(userRepository.save(user));
    }
}
