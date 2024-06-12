import Link from 'next/link';

type PostProps = {
  post: {
    id: number;
    title: string;
  };
};

const Post: React.FC<PostProps> = ({ post }) => (
  <tr>
    <td>{post.id}</td>
    <td>
      <Link href={`/post/${post.id}`}>{post.title}</Link>
    </td>
  </tr>
);

export default Post;
